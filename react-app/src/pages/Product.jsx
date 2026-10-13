import { useEffect, useMemo, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useNavigate, useParams } from 'react-router'
import { ChevronRight, Crown, ShieldCheck, Truck } from 'lucide-react'
import { fetchProduct, selectProduct, selectProductMissing, selectProducts, selectTypes } from '../features/catalogSlice'
import { fetchReviews } from '../features/reviewsSlice'
import { selectUser } from '../features/sessionSlice'
import useAddToCart from '../hooks/useAddToCart'
import ProductCard from '../components/ProductCard'
import ProductImage from '../components/ProductImage'
import Price from '../components/Price'
import QuantitySelect from '../components/QuantitySelect'
import Shelf from '../components/Shelf'
import Stars from '../components/Stars'
import { money } from '../utils/format'
import NotFound from './NotFound'
import Reviews from './Reviews'
import './Product.css'

// Keyed by product so the quantity picker starts fresh on each page
export default function Product() {
  const { productId } = useParams()
  return <ProductView key={productId} id={Number(productId)} />
}

function ProductView({ id }) {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const user = useSelector(selectUser)
  const product = useSelector((state) => selectProduct(state, id))
  const missing = useSelector((state) => selectProductMissing(state, id))
  const type = useSelector(selectTypes).find((t) => t.id === product?.type_id)
  const allProducts = useSelector(selectProducts)
  const { add, adding } = useAddToCart()
  const [quantity, setQuantity] = useState(1)

  useEffect(() => {
    dispatch(fetchProduct(id))
    dispatch(fetchReviews(id))
  }, [dispatch, id])

  const related = useMemo(
    () => allProducts.filter((p) => p.type_id === product?.type_id && p.id !== id && p.image && !p.image.startsWith('data:')),
    [allProducts, product?.type_id, id])

  if (missing || Number.isNaN(id)) return <NotFound />
  if (!product) {
    return (
      <div className="container product-page" aria-busy="true" aria-label="Loading product">
        <div className="skeleton" style={{ height: 480 }} />
      </div>
    )
  }

  const shippingNote = user?.isPrime
    ? <><Crown size={15} /> <strong>FREE shipping</strong> with your Prime membership</>
    : <><Truck size={15} /> Shipping is 5% of your items total. <Link to="/prime">Prime ships free.</Link></>

  const buyNow = async () => {
    if (await add(product, quantity)) navigate('/cart')
  }

  return (
    <div className="container product-page">
      <nav className="breadcrumb" aria-label="Breadcrumb">
        <Link to="/">Home</Link>
        {type && <><ChevronRight size={14} aria-hidden="true" /><Link to={`/category/${type.id}`}>{type.name}</Link></>}
      </nav>

      <div className="product-layout">
        <div className="product-media card">
          <ProductImage src={product.image} alt={product.name} className="product-media__image" loading="eager" />
        </div>

        <div className="product-info">
          <h1>{product.name}</h1>
          <a href="#reviews" className="product-info__rating">
            {product.review_count > 0
              ? <Stars value={product.rating} count={product.review_count} showValue />
              : <span className="muted">No reviews yet</span>}
          </a>
          <hr />
          <div className="product-info__price">
            <Price value={product.price} size="lg" />
          </div>
          <h2 className="product-info__about">About this item</h2>
          <p className="product-info__description">{product.description}</p>
        </div>

        <aside className="buybox card" aria-label="Purchase options">
          <Price value={product.price} size="lg" />
          <p className="buybox__shipping">{shippingNote}</p>
          <p className="buybox__stock">In stock</p>
          <div className="buybox__qty">
            <label htmlFor="qty" className="sr-only">Quantity</label>
            <QuantitySelect id="qty" value={quantity} onChange={setQuantity} />
            <span className="muted">Total {money(product.price * quantity)}</span>
          </div>
          <button type="button" className="btn btn--primary btn--lg btn--block" disabled={adding}
            onClick={() => add(product, quantity)}>Add to cart</button>
          <button type="button" className="btn btn--buy btn--lg btn--block" disabled={adding}
            onClick={buyNow}>Buy now</button>
          <p className="buybox__secure"><ShieldCheck size={15} /> Secure demo checkout. No payment is taken.</p>
        </aside>
      </div>

      <Reviews product={product} />

      {related.length > 0 && (
        <Shelf title={`More in ${type?.name ?? 'this category'}`} seeAll={type && `/category/${type.id}`}>
          {related.slice(0, 12).map((p) => <ProductCard key={p.id} product={p} compact />)}
        </Shelf>
      )}
    </div>
  )
}

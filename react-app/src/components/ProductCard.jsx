import { Link } from 'react-router'
import { ShoppingCart } from 'lucide-react'
import ProductImage from './ProductImage'
import Stars from './Stars'
import Price from './Price'
import useAddToCart from '../hooks/useAddToCart'

export default function ProductCard({ product, compact = false }) {
  const { add, adding } = useAddToCart()

  return (
    <article className={`product-card ${compact ? 'product-card--compact' : ''}`}>
      <Link to={`/product/${product.id}`} className="product-card__media" tabIndex={-1} aria-hidden="true">
        <ProductImage src={product.image} className="product-card__image" />
      </Link>
      <div className="product-card__body">
        <h3 className="product-card__title">
          <Link to={`/product/${product.id}`}>{product.name}</Link>
        </h3>
        {product.review_count > 0
          ? <Stars value={product.rating} count={product.review_count} size={14} />
          : <span className="muted product-card__norating">No reviews yet</span>}
        <Price value={product.price} />
        {!compact && (
          <button type="button" className="btn btn--primary btn--sm product-card__add"
            onClick={() => add(product)} disabled={adding}>
            <ShoppingCart size={15} aria-hidden="true" /> Add to cart
          </button>
        )}
      </div>
    </article>
  )
}

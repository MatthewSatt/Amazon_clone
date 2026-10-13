import { useMemo, useState } from 'react'
import { useSelector } from 'react-redux'
import { useParams, useSearchParams } from 'react-router'
import { SearchX } from 'lucide-react'
import { selectCatalogStatus, selectProducts, selectTypes } from '../features/catalogSlice'
import ProductCard from '../components/ProductCard'
import EmptyState from '../components/EmptyState'
import { pluralize } from '../utils/format'
import NotFound from './NotFound'
import './Listing.css'

const SORTS = {
  featured: { label: 'Featured', compare: (a, b) => a.id - b.id },
  'price-asc': { label: 'Price: low to high', compare: (a, b) => a.price - b.price },
  'price-desc': { label: 'Price: high to low', compare: (a, b) => b.price - a.price },
  rating: { label: 'Top rated', compare: (a, b) => (b.rating ?? 0) - (a.rating ?? 0) || b.review_count - a.review_count },
}

const PRICE_BANDS = [
  { id: 'all', label: 'Any price', test: () => true },
  { id: 'u25', label: 'Under $25', test: (p) => p.price < 25 },
  { id: '25-50', label: '$25 – $50', test: (p) => p.price >= 25 && p.price < 50 },
  { id: '50-100', label: '$50 – $100', test: (p) => p.price >= 50 && p.price < 100 },
  { id: '100+', label: '$100 & above', test: (p) => p.price >= 100 },
]

function Listing({ title, subtitle, products, loading }) {
  const [sort, setSort] = useState('featured')
  const [band, setBand] = useState('all')

  const visible = useMemo(() => {
    const test = PRICE_BANDS.find((b) => b.id === band).test
    return products.filter(test).sort(SORTS[sort].compare)
  }, [products, sort, band])

  return (
    <div className="container listing">
      <header className="listing__head">
        <div>
          <h1 className="page-title">{title}</h1>
          <p className="muted">{subtitle}</p>
        </div>
        <div className="listing__sort">
          <label htmlFor="sort" className="muted">Sort by</label>
          <select id="sort" className="select select--sm" value={sort} onChange={(e) => setSort(e.target.value)}>
            {Object.entries(SORTS).map(([key, { label }]) => <option key={key} value={key}>{label}</option>)}
          </select>
        </div>
      </header>

      <div className="listing__chips" role="radiogroup" aria-label="Filter by price">
        {PRICE_BANDS.map((b) => (
          <button key={b.id} type="button" role="radio" aria-checked={band === b.id}
            className={`chip ${band === b.id ? 'is-active' : ''}`} onClick={() => setBand(b.id)}>
            {b.label}
          </button>
        ))}
      </div>

      {loading ? (
        <div className="product-grid" aria-busy="true">
          {Array.from({ length: 8 }, (_, i) => <div key={i} className="skeleton" style={{ height: 380 }} />)}
        </div>
      ) : visible.length > 0 ? (
        <div className="product-grid">
          {visible.map((product) => <ProductCard key={product.id} product={product} />)}
        </div>
      ) : (
        <EmptyState icon={SearchX} title="No products match" action={{ to: '/', label: 'Back to home' }}>
          Try a different price range or search term.
        </EmptyState>
      )}
    </div>
  )
}

export function CategoryPage() {
  const { typeId } = useParams()
  const types = useSelector(selectTypes)
  const products = useSelector(selectProducts)
  const status = useSelector(selectCatalogStatus)
  const type = types.find((t) => t.id === Number(typeId))

  const items = useMemo(() => products.filter((p) => p.type_id === Number(typeId)), [products, typeId])

  if (status === 'ready' && !type) return <NotFound />
  return (
    <Listing key={typeId} title={type?.name ?? 'Loading…'} loading={status !== 'ready'}
      subtitle={status === 'ready' ? pluralize(items.length, 'product') : ''} products={items} />
  )
}

export function SearchPage() {
  const [params] = useSearchParams()
  const query = (params.get('q') ?? '').trim()
  const typeId = params.get('type')
  const products = useSelector(selectProducts)
  const types = useSelector(selectTypes)
  const status = useSelector(selectCatalogStatus)

  const results = useMemo(() => {
    const needle = query.toLowerCase()
    return products.filter((p) =>
      p.name.toLowerCase().includes(needle) && (!typeId || p.type_id === Number(typeId)))
  }, [products, query, typeId])

  const typeName = types.find((t) => t.id === Number(typeId))?.name

  if (!query) {
    return (
      <div className="container">
        <EmptyState icon={SearchX} title="What are you looking for?" action={{ to: '/', label: 'Browse the store' }}>
          Type a product name in the search bar above.
        </EmptyState>
      </div>
    )
  }

  return (
    <Listing key={`${query}|${typeId}`} title={`Results for “${query}”`} loading={status !== 'ready'}
      subtitle={status === 'ready'
        ? `${pluralize(results.length, 'result')}${typeName ? ` in ${typeName}` : ''}`
        : ''}
      products={results} />
  )
}

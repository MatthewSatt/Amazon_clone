import { useId, useMemo, useRef, useState } from 'react'
import { useSelector } from 'react-redux'
import { useNavigate, useSearchParams } from 'react-router'
import { Search } from 'lucide-react'
import { selectProducts, selectTypes } from '../features/catalogSlice'
import ProductImage from './ProductImage'

const MAX_SUGGESTIONS = 6

export default function SearchBox() {
  const navigate = useNavigate()
  const [params] = useSearchParams()
  const products = useSelector(selectProducts)
  const types = useSelector(selectTypes)
  const listId = useId()
  const wrapper = useRef(null)

  const [query, setQuery] = useState(params.get('q') ?? '')
  const [typeId, setTypeId] = useState(params.get('type') ?? '')
  const [open, setOpen] = useState(false)
  const [active, setActive] = useState(-1)

  const suggestions = useMemo(() => {
    const needle = query.trim().toLowerCase()
    if (needle.length < 2) return []
    return products
      .filter((p) => (!typeId || p.type_id === Number(typeId)) && p.name.toLowerCase().includes(needle))
      .slice(0, MAX_SUGGESTIONS)
  }, [products, query, typeId])

  const showList = open && suggestions.length > 0

  const submit = (event) => {
    event.preventDefault()
    const q = query.trim()
    if (!q) return
    setOpen(false)
    const search = new URLSearchParams({ q })
    if (typeId) search.set('type', typeId)
    navigate(`/search?${search}`)
  }

  const choose = (product) => {
    setOpen(false)
    setQuery('')
    navigate(`/product/${product.id}`)
  }

  const onKeyDown = (event) => {
    if (event.key === 'ArrowDown' && suggestions.length) {
      event.preventDefault()
      setOpen(true)
      setActive((i) => (i + 1) % suggestions.length)
    } else if (event.key === 'ArrowUp' && suggestions.length) {
      event.preventDefault()
      setActive((i) => (i <= 0 ? suggestions.length - 1 : i - 1))
    } else if (event.key === 'Escape') {
      setOpen(false)
    } else if (event.key === 'Enter' && showList && active >= 0) {
      event.preventDefault()
      choose(suggestions[active])
    }
  }

  return (
    <form className="searchbox" role="search" onSubmit={submit} ref={wrapper}
      onBlur={(event) => { if (!wrapper.current.contains(event.relatedTarget)) setOpen(false) }}>
      <label className="sr-only" htmlFor="search-category">Search category</label>
      <select id="search-category" className="searchbox__type" value={typeId} onChange={(e) => setTypeId(e.target.value)}>
        <option value="">All</option>
        {types.map((type) => <option key={type.id} value={type.id}>{type.name}</option>)}
      </select>
      <label className="sr-only" htmlFor="search-input">Search products</label>
      <input id="search-input" className="searchbox__input" type="search" placeholder="Search products"
        autoComplete="off" value={query} role="combobox" aria-expanded={showList} aria-controls={listId}
        aria-autocomplete="list" aria-activedescendant={active >= 0 ? `${listId}-${active}` : undefined}
        onChange={(e) => { setQuery(e.target.value); setActive(-1); setOpen(true) }}
        onFocus={() => setOpen(true)} onKeyDown={onKeyDown} />
      <button type="submit" className="searchbox__submit" aria-label="Search"><Search size={20} /></button>

      {showList && (
        <ul className="searchbox__list" id={listId} role="listbox">
          {suggestions.map((product, i) => (
            <li key={product.id} id={`${listId}-${i}`} role="option" aria-selected={i === active}
              className={i === active ? 'is-active' : ''} onMouseEnter={() => setActive(i)}
              onMouseDown={(event) => event.preventDefault()} onClick={() => choose(product)}>
              <ProductImage src={product.image} className="searchbox__thumb" />
              <span>{product.name}</span>
            </li>
          ))}
        </ul>
      )}
    </form>
  )
}

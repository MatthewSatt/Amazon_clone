import { useEffect, useMemo, useState } from 'react'
import { useSelector } from 'react-redux'
import { Link } from 'react-router'
import { ChevronLeft, ChevronRight, Crown, Pause, Play } from 'lucide-react'
import { selectCatalogStatus, selectProducts, selectTypes } from '../features/catalogSlice'
import { selectUser } from '../features/sessionSlice'
import ProductCard from '../components/ProductCard'
import ProductImage from '../components/ProductImage'
import Shelf from '../components/Shelf'
import './Home.css'

const SLIDES = [
  { type: 'Electronics', kicker: 'Tech picks', title: 'Upgrade your everyday gear', text: 'Tablets, consoles, headphones and more, rated by real shoppers.', tone: 'indigo' },
  { type: 'Books', kicker: 'Reading list', title: 'Your next favourite story', text: 'From page-turning thrillers to practical bestsellers.', tone: 'teal' },
  { type: 'Sports', kicker: 'Get moving', title: 'Gear up for the season', text: 'Equipment and apparel for every kind of workout.', tone: 'ember' },
]

const SHELVES = ['Books', 'Electronics', 'Outdoors']

const usable = (product) => product.image && !product.image.startsWith('data:')
const bestOf = (list) => [...list].sort((a, b) => (b.rating ?? 0) - (a.rating ?? 0) || a.id - b.id)

function Hero({ slides }) {
  const [index, setIndex] = useState(0)
  const [paused, setPaused] = useState(false)
  const [hovering, setHovering] = useState(false)
  const reduceMotion = typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches
  const running = !paused && !hovering && !reduceMotion && slides.length > 1

  useEffect(() => {
    if (!running) return
    const timer = setTimeout(() => setIndex((i) => (i + 1) % slides.length), 6000)
    return () => clearTimeout(timer)
  }, [index, running, slides.length])

  const go = (n) => setIndex((n + slides.length) % slides.length)

  return (
    <section className="hero" aria-roledescription="carousel" aria-label="Featured collections"
      onMouseEnter={() => setHovering(true)} onMouseLeave={() => setHovering(false)}>
      {slides.map((slide, i) => (
        <div key={slide.type} className={`hero__slide hero__slide--${slide.tone} ${i === index ? 'is-active' : ''}`}
          role="group" aria-roledescription="slide" aria-label={`${i + 1} of ${slides.length}`} aria-hidden={i !== index}>
          <div className="container hero__inner">
            <div className="hero__copy">
              <span className="hero__kicker">{slide.kicker}</span>
              <h1>{slide.title}</h1>
              <p>{slide.text}</p>
              <Link to={`/category/${slide.typeId}`} className="btn btn--primary btn--lg" tabIndex={i === index ? 0 : -1}>
                Shop {slide.type}
              </Link>
            </div>
            <Link to={`/product/${slide.product.id}`} className="hero__product" tabIndex={-1} aria-hidden="true">
              <ProductImage src={slide.product.image} className="hero__image" loading="eager" />
            </Link>
          </div>
        </div>
      ))}

      <div className="hero__controls">
        <button type="button" className="hero__btn" onClick={() => go(index - 1)} aria-label="Previous slide"><ChevronLeft size={20} /></button>
        <div className="hero__dots">
          {slides.map((slide, i) => (
            <button key={slide.type} type="button" className={`hero__dot ${i === index ? 'is-active' : ''}`}
              onClick={() => go(i)} aria-label={`Go to slide ${i + 1}`} aria-current={i === index} />
          ))}
        </div>
        <button type="button" className="hero__btn" onClick={() => go(index + 1)} aria-label="Next slide"><ChevronRight size={20} /></button>
        <button type="button" className="hero__btn" onClick={() => setPaused((p) => !p)}
          aria-label={paused ? 'Play slideshow' : 'Pause slideshow'}>
          {paused ? <Play size={16} /> : <Pause size={16} />}
        </button>
      </div>
    </section>
  )
}

function CategoryTile({ type, products }) {
  const preview = products.filter(usable).slice(0, 4)
  return (
    <article className="tile card">
      <h2>{type.name}</h2>
      <Link to={`/category/${type.id}`} className="tile__grid" aria-label={`Shop ${type.name}`}>
        {preview.map((product) => <ProductImage key={product.id} src={product.image} className="tile__img" />)}
      </Link>
      <Link to={`/category/${type.id}`} className="tile__link">Shop {type.name.toLowerCase()}</Link>
    </article>
  )
}

function HomeSkeleton() {
  return (
    <div className="container" aria-busy="true" aria-label="Loading">
      <div className="skeleton" style={{ height: 300, marginBottom: 24 }} />
      <div className="tiles">
        {Array.from({ length: 8 }, (_, i) => <div key={i} className="skeleton" style={{ height: 340 }} />)}
      </div>
    </div>
  )
}

export default function Home() {
  const products = useSelector(selectProducts)
  const types = useSelector(selectTypes)
  const status = useSelector(selectCatalogStatus)
  const user = useSelector(selectUser)

  const byType = useMemo(() => {
    const map = new Map()
    for (const product of products) {
      if (!map.has(product.type_id)) map.set(product.type_id, [])
      map.get(product.type_id).push(product)
    }
    return map
  }, [products])

  const slides = useMemo(() => SLIDES.flatMap((slide) => {
    const type = types.find((t) => t.name === slide.type)
    const product = type && bestOf((byType.get(type.id) ?? []).filter(usable))[0]
    return product ? [{ ...slide, typeId: type.id, product }] : []
  }), [types, byType])

  const topRated = useMemo(
    () => bestOf(products.filter((p) => usable(p) && p.review_count > 0)).slice(0, 12), [products])

  if (status === 'error') {
    return (
      <div className="container">
        <div className="alert alert--error" role="alert">We couldn’t load the store. Please refresh the page.</div>
      </div>
    )
  }
  if (status !== 'ready') return <HomeSkeleton />

  return (
    <>
      {slides.length > 0 && <Hero slides={slides} />}

      <div className="container home">
        <div className="tiles">
          {types.map((type) => <CategoryTile key={type.id} type={type} products={byType.get(type.id) ?? []} />)}
          {!user?.isPrime && (
            <article className="tile tile--prime">
              <Crown size={34} aria-hidden="true" />
              <h2>Free shipping with Prime</h2>
              <p>Skip the 5% shipping fee on every order.</p>
              <Link to="/prime" className="btn btn--primary">Explore Prime</Link>
            </article>
          )}
        </div>

        {topRated.length > 0 && (
          <Shelf title="Top rated by customers">
            {topRated.map((product) => <ProductCard key={product.id} product={product} compact />)}
          </Shelf>
        )}

        {SHELVES.map((name) => {
          const type = types.find((t) => t.name === name)
          const items = type ? bestOf(byType.get(type.id) ?? []).filter(usable) : []
          return items.length > 0 && (
            <Shelf key={name} title={`Best in ${name}`} seeAll={`/category/${type.id}`}>
              {items.map((product) => <ProductCard key={product.id} product={product} compact />)}
            </Shelf>
          )
        })}
      </div>
    </>
  )
}

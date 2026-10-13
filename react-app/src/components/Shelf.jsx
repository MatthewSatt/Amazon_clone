import { useRef } from 'react'
import { Link } from 'react-router'
import { ChevronLeft, ChevronRight } from 'lucide-react'

// A titled, horizontally scrolling row of cards
export default function Shelf({ title, seeAll, children }) {
  const track = useRef(null)
  const scroll = (direction) => {
    const el = track.current
    el.scrollBy({ left: direction * el.clientWidth * 0.85, behavior: 'smooth' })
  }

  return (
    <section className="shelf card" aria-label={title}>
      <header className="shelf__header">
        <h2>{title}</h2>
        {seeAll && <Link to={seeAll}>See all</Link>}
      </header>
      <div className="shelf__body">
        <button type="button" className="shelf__arrow shelf__arrow--prev" onClick={() => scroll(-1)} aria-label={`Scroll ${title} left`}>
          <ChevronLeft size={22} />
        </button>
        <div className="shelf__track" ref={track} tabIndex={-1}>{children}</div>
        <button type="button" className="shelf__arrow shelf__arrow--next" onClick={() => scroll(1)} aria-label={`Scroll ${title} right`}>
          <ChevronRight size={22} />
        </button>
      </div>
    </section>
  )
}

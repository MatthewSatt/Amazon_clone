import { useState } from 'react'
import { Star } from 'lucide-react'

const LABELS = ['Terrible', 'Poor', 'Okay', 'Good', 'Excellent']

// Interactive 1-5 star input (a radio group, so it works with the keyboard)
export default function StarPicker({ value, onChange, invalid }) {
  const [hover, setHover] = useState(0)
  const shown = hover || value

  return (
    <div>
      <div className="star-picker" role="radiogroup" aria-label="Rating" aria-invalid={invalid || undefined}
        onMouseLeave={() => setHover(0)}>
        {LABELS.map((label, i) => {
          const n = i + 1
          return (
            <label key={n} className="star-picker__star" onMouseEnter={() => setHover(n)}>
              <input type="radio" name="rating" value={n} checked={value === n}
                onChange={() => onChange(n)} className="sr-only" />
              <Star size={32} className={n <= shown ? 'is-on' : ''} />
              <span className="sr-only">{n} star{n > 1 ? 's' : ''}, {label}</span>
            </label>
          )
        })}
      </div>
      <div className="star-picker__label muted" aria-hidden="true">{shown ? LABELS[shown - 1] : 'Select a rating'}</div>
    </div>
  )
}

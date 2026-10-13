import { useDispatch, useSelector } from 'react-redux'
import { Link, useNavigate } from 'react-router'
import { Check, Crown, Gift, Music, PlayCircle, Truck } from 'lucide-react'
import { selectUser, setPrime } from '../features/sessionSlice'
import { firstError } from '../features/thunks'
import { notify } from '../features/toastsSlice'
import { useState } from 'react'
import './Prime.css'

const BENEFITS = [
  { icon: Truck, title: 'Free shipping', text: 'Every order ships free: no 5% fee at checkout, no minimum.' },
  { icon: PlayCircle, title: 'Prime Video', text: 'Unlimited streaming of movies and TV episodes.' },
  { icon: Music, title: 'Prime Music', text: 'Ad-free listening to a catalogue of songs and playlists.' },
  { icon: Gift, title: 'Member perks', text: 'Early access to deals and exclusive member offers.' },
]

export default function Prime() {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const user = useSelector(selectUser)
  const [busy, setBusy] = useState(false)

  const toggle = async (next) => {
    if (!user) {
      navigate('/login', { state: { from: '/prime' } })
      return
    }
    setBusy(true)
    const result = await dispatch(setPrime(next))
    setBusy(false)
    dispatch(setPrime.fulfilled.match(result)
      ? notify(next ? 'Welcome to Prime! Shipping is now free.' : 'Your Prime membership has ended.')
      : notify(firstError(result.payload), 'error'))
  }

  const member = Boolean(user?.isPrime)

  return (
    <div className="prime">
      <section className="prime__hero">
        <div className="container prime__hero-inner">
          <span className="prime__badge"><Crown size={16} /> Prime</span>
          <h1>{member ? 'You’re a Prime member' : 'Everything ships free with Prime'}</h1>
          <p>
            {member
              ? 'Enjoy free shipping on every order, plus streaming and member perks.'
              : 'Join in one click and skip the shipping fee on every order. This is a demo, so membership is free.'}
          </p>
          <div className="prime__cta">
            {member ? (
              <>
                <Link to="/" className="btn btn--primary btn--lg">Start shopping</Link>
                <button type="button" className="btn btn--lg prime__leave" disabled={busy} onClick={() => toggle(false)}>
                  End membership
                </button>
              </>
            ) : (
              <button type="button" className="btn btn--primary btn--lg" disabled={busy} onClick={() => toggle(true)}>
                {user ? (busy ? 'Joining…' : 'Join Prime') : 'Sign in to join Prime'}
              </button>
            )}
          </div>
          <ul className="prime__checks">
            <li><Check size={16} /> No fees, ever</li>
            <li><Check size={16} /> Cancel any time</li>
            <li><Check size={16} /> Applies instantly at checkout</li>
          </ul>
        </div>
      </section>

      <section className="container prime__benefits" aria-label="Prime benefits">
        {BENEFITS.map(({ icon: Icon, title, text }) => (
          <article key={title} className="card prime__benefit">
            <span className="prime__icon"><Icon size={24} /></span>
            <h2>{title}</h2>
            <p>{text}</p>
          </article>
        ))}
      </section>
    </div>
  )
}

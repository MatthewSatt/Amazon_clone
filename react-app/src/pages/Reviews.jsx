import { useMemo, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useLocation, useNavigate } from 'react-router'
import { MessageSquarePlus, Pencil, Trash2 } from 'lucide-react'
import { selectUser } from '../features/sessionSlice'
import { deleteReview, selectReviews } from '../features/reviewsSlice'
import { firstError } from '../features/thunks'
import { notify } from '../features/toastsSlice'
import Modal from '../components/Modal'
import Stars from '../components/Stars'
import { longDate, pluralize } from '../utils/format'
import ReviewModal from './ReviewModal'

function Histogram({ reviews }) {
  const total = reviews.length
  return (
    <ul className="histogram" aria-label="Rating breakdown">
      {[5, 4, 3, 2, 1].map((star) => {
        const count = reviews.filter((r) => r.rating === star).length
        const percent = total ? Math.round((count / total) * 100) : 0
        return (
          <li key={star}>
            <span>{star} star</span>
            <span className="histogram__bar"><span style={{ width: `${percent}%` }} /></span>
            <span className="muted">{percent}%</span>
          </li>
        )
      })}
    </ul>
  )
}

export default function Reviews({ product }) {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const location = useLocation()
  const user = useSelector(selectUser)
  const reviews = useSelector((state) => selectReviews(state, product.id))
  const [editing, setEditing] = useState(null) // null | 'new' | review
  const [deleting, setDeleting] = useState(null)

  const mine = useMemo(() => reviews?.find((r) => r.user_id === user?.id), [reviews, user])

  const write = () => {
    if (!user) {
      dispatch(notify('Sign in to write a review.', 'error'))
      navigate('/login', { state: { from: location.pathname } })
      return
    }
    setEditing(mine ?? 'new')
  }

  const confirmDelete = async () => {
    const result = await dispatch(deleteReview({ id: deleting.id, productId: product.id }))
    setDeleting(null)
    dispatch(deleteReview.fulfilled.match(result)
      ? notify('Your review was deleted.')
      : notify(firstError(result.payload), 'error'))
  }

  const average = product.rating ?? 0

  return (
    <section className="reviews" id="reviews" aria-labelledby="reviews-title">
      <aside className="reviews__summary">
        <h2 id="reviews-title">Customer reviews</h2>
        {product.review_count > 0 ? (
          <>
            <div className="reviews__avg">
              <strong>{average.toFixed(1)}</strong>
              <div>
                <Stars value={average} size={18} />
                <div className="muted">{pluralize(product.review_count, 'rating')}</div>
              </div>
            </div>
            {reviews && <Histogram reviews={reviews} />}
          </>
        ) : (
          <p className="muted">No reviews yet.</p>
        )}
        <button type="button" className="btn btn--secondary btn--block" onClick={write}>
          {mine ? <><Pencil size={16} /> Edit your review</> : <><MessageSquarePlus size={16} /> Write a review</>}
        </button>
      </aside>

      <div className="reviews__list">
        {!reviews && <div className="skeleton" style={{ height: 120 }} aria-busy="true" />}
        {reviews?.length === 0 && (
          <div className="reviews__empty">
            <h3>Be the first to review this product</h3>
            <p className="muted">Share what you think and help other shoppers decide.</p>
          </div>
        )}
        {reviews?.map((review) => (
          <article key={review.id} className="review">
            <header className="review__head">
              <span className="review__avatar" aria-hidden="true">{review.author?.[0]?.toUpperCase()}</span>
              <span className="review__author">
                {review.author}{review.user_id === user?.id && <span className="badge">You</span>}
              </span>
            </header>
            <div className="review__meta">
              <Stars value={review.rating} size={15} />
              <h3>{review.title}</h3>
            </div>
            <p className="muted review__date">Reviewed on {longDate(review.created_at)}</p>
            <p className="review__body">{review.body}</p>
            {review.user_id === user?.id && (
              <div className="review__actions">
                <button type="button" className="btn btn--ghost btn--sm" onClick={() => setEditing(review)}>
                  <Pencil size={14} /> Edit
                </button>
                <button type="button" className="btn btn--danger btn--sm" onClick={() => setDeleting(review)}>
                  <Trash2 size={14} /> Delete
                </button>
              </div>
            )}
          </article>
        ))}
      </div>

      {editing && (
        <ReviewModal product={product} review={editing === 'new' ? undefined : editing} onClose={() => setEditing(null)} />
      )}
      {deleting && (
        <Modal title="Delete this review?" size="sm" onClose={() => setDeleting(null)}>
          <p className="muted">This can’t be undone.</p>
          <div className="modal-actions">
            <button type="button" className="btn btn--secondary" onClick={() => setDeleting(null)}>Keep it</button>
            <button type="button" className="btn btn--dark" onClick={confirmDelete}>Delete review</button>
          </div>
        </Modal>
      )}
    </section>
  )
}

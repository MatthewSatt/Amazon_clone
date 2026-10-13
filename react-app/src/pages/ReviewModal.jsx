import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { saveReview } from '../features/reviewsSlice'
import { notify } from '../features/toastsSlice'
import Modal from '../components/Modal'
import StarPicker from '../components/StarPicker'
import { Field } from './AuthForm'

// Write a review, or edit `review` when one is passed
export default function ReviewModal({ product, review, onClose }) {
  const dispatch = useDispatch()
  const [rating, setRating] = useState(review?.rating ?? 0)
  const [title, setTitle] = useState(review?.title ?? '')
  const [body, setBody] = useState(review?.body ?? '')
  const [errors, setErrors] = useState({})
  const [busy, setBusy] = useState(false)

  const submit = async (event) => {
    event.preventDefault()
    setBusy(true)
    setErrors({})
    const result = await dispatch(saveReview({ id: review?.id, productId: product.id, rating, title, body }))
    setBusy(false)
    if (saveReview.rejected.match(result)) {
      setErrors(result.payload?.errors ?? { form: ['Something went wrong. Please try again.'] })
      return
    }
    dispatch(notify(review ? 'Your review was updated.' : 'Thanks! Your review was posted.'))
    onClose()
  }

  return (
    <Modal title={review ? 'Edit your review' : 'Write a review'} onClose={onClose}>
      <form onSubmit={submit} noValidate>
        <p className="muted" style={{ marginBottom: 16 }}>{product.name}</p>
        {errors.form && <div className="alert alert--error" role="alert" style={{ marginBottom: 16 }}>{errors.form[0]}</div>}

        <div className="field">
          <span className="field__label">Overall rating</span>
          <StarPicker value={rating} onChange={setRating} invalid={Boolean(errors.rating)} />
          {errors.rating && <span className="field__error">{errors.rating[0]}</span>}
        </div>
        <Field label="Headline" id="review-title" error={errors.title?.[0]}>
          <input id="review-title" className="input" value={title} maxLength={255} placeholder="What’s most important to know?"
            onChange={(e) => setTitle(e.target.value)} aria-invalid={Boolean(errors.title)} />
        </Field>
        <Field label="Your review" id="review-body" error={errors.body?.[0]}>
          <textarea id="review-body" className="textarea" value={body} maxLength={5000}
            placeholder="What did you like or dislike? How did you use it?"
            onChange={(e) => setBody(e.target.value)} aria-invalid={Boolean(errors.body)} />
        </Field>

        <div className="modal-actions">
          <button type="button" className="btn btn--secondary" onClick={onClose}>Cancel</button>
          <button type="submit" className="btn btn--primary" disabled={busy}>
            {busy ? 'Saving…' : review ? 'Save changes' : 'Post review'}
          </button>
        </div>
      </form>
    </Modal>
  )
}

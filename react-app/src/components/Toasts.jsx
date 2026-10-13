import { useDispatch, useSelector } from 'react-redux'
import { CheckCircle2, AlertCircle, X } from 'lucide-react'
import { toastDismissed } from '../features/toastsSlice'

export default function Toasts() {
  const toasts = useSelector((state) => state.toasts)
  const dispatch = useDispatch()

  return (
    <div className="toasts" role="status" aria-live="polite">
      {toasts.map((toast) => (
        <div key={toast.id} className={`toast toast--${toast.kind}`}>
          {toast.kind === 'error' ? <AlertCircle size={20} /> : <CheckCircle2 size={20} />}
          <span>{toast.message}</span>
          <button type="button" className="toast__close" aria-label="Dismiss"
            onClick={() => dispatch(toastDismissed(toast.id))}>
            <X size={16} />
          </button>
        </div>
      ))}
    </div>
  )
}

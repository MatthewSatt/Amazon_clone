import { useEffect, useRef } from 'react'
import { X } from 'lucide-react'

// Built on the native <dialog>: focus trapping, Esc to close and the
// backdrop come from the browser
export default function Modal({ title, onClose, children, size = 'md' }) {
  const ref = useRef(null)

  useEffect(() => {
    const dialog = ref.current
    dialog.showModal()
    document.body.style.overflow = 'hidden'
    return () => {
      document.body.style.overflow = ''
      dialog.close()
    }
  }, [])

  return (
    <dialog ref={ref} className={`modal modal--${size}`} aria-labelledby="modal-title"
      onCancel={(event) => { event.preventDefault(); onClose() }}
      onMouseDown={(event) => { if (event.target === ref.current) onClose() }}>
      <div className="modal__panel">
        <header className="modal__header">
          <h2 id="modal-title">{title}</h2>
          <button type="button" className="icon-btn" onClick={onClose} aria-label="Close">
            <X size={20} />
          </button>
        </header>
        <div className="modal__body">{children}</div>
      </div>
    </dialog>
  )
}

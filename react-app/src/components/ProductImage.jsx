import { useState } from 'react'
import { ImageOff } from 'lucide-react'

// Product photos are hot-linked, so show a tidy placeholder when one fails
export default function ProductImage({ src, alt = '', className = '', ...rest }) {
  const [failedSrc, setFailedSrc] = useState(null)

  if (!src || failedSrc === src) {
    return (
      <div className={`image-fallback ${className}`} role={alt ? 'img' : undefined} aria-label={alt || undefined}>
        <ImageOff size={28} aria-hidden="true" />
      </div>
    )
  }
  return (
    <img src={src} alt={alt} className={className} loading="lazy" referrerPolicy="no-referrer"
      onError={() => setFailedSrc(src)} {...rest} />
  )
}

const OPTIONS = Array.from({ length: 10 }, (_, i) => i + 1)

export default function QuantitySelect({ value, onChange, disabled, id }) {
  return (
    <select id={id} className="select select--sm" value={value} disabled={disabled}
      onChange={(event) => onChange(Number(event.target.value))} aria-label="Quantity">
      {OPTIONS.map((n) => <option key={n} value={n}>Qty: {n}</option>)}
    </select>
  )
}

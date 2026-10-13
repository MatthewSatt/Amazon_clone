const currency = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })

export const money = (value) => currency.format(value ?? 0)

export const splitPrice = (value) => {
  const [whole, cents] = (value ?? 0).toFixed(2).split('.')
  return { whole: Number(whole).toLocaleString('en-US'), cents }
}

export const longDate = (iso) =>
  iso ? new Date(iso).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }) : ''

export const pluralize = (count, word) => `${count} ${word}${count === 1 ? '' : 's'}`

export const slug = (text) => text.toLowerCase().replace(/[^a-z0-9]+/g, '-')

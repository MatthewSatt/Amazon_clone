import React from 'react'
import './SubTotal.css'
import CurrencyFormat from 'react-currency-format'
import {useSelector} from 'react-redux'

function SubTotal() {
  const user = useSelector(state => state.session.user)
  const products = useSelector(state => state.products)
  const getBasketTotal = () => {
    console.log("basket total")
  }
  return (
    <div className='subtotal'>
        <CurrencyFormat
        renderText={(value) => (
            <>
            <p>
                SubTotal ({5} items): <strong>{value}</strong>
            </p>
            <small className='subtotal__gift'>
                <input type='checkbox' />
                This order contains gift
            </small>
            </>
        )}
        decimalScale={2}
        value={4}
        displayType={"text"}
        thousandSeparator={true}
        prefix={'$'}
        />
        <button>Proceed to Checkout</button>
    </div>

  );
}

export default SubTotal

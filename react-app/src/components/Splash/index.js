import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getProducts } from '../../store/products'
import {getTypesThunk} from '../../store/types'
import './Splash.css'

function Splash() {
    const dispatch = useDispatch()
    const products = useSelector(state => state.productReducer)
    const types = useSelector(state => state.typeReducer)


    useEffect(() => {
        dispatch(getProducts())
        dispatch(getTypesThunk())
    }, [dispatch])
  return (
    <div className='splashpage'>
        <div className='splashnav'>
            {types && types.map(type => (
                <div key={type.id}>
                    <h1 className='productcategories'>{type.name}
                    <div className='scrolloptions'>
                    <p>left</p>
                    <p>right</p>
                    </div>
                    </h1>

                    <div className='productline'>
                    {products.filter(product => product.type_id == type.id).map(filteredProducts => (
                        <div className='eachproduct'>
                            <p className='producttitle'>{filteredProducts.name}</p>
                            <p><small>$</small>{filteredProducts.price}</p>

                        </div>
                    ))}
                    </div>
                </div>

            ))}
        </div>
    </div>
  )
}

export default Splash

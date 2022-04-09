import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getProducts } from '../../store/products'
import {getTypesThunk} from '../../store/types'
import { FaArrowAltCircleLeft, FaArrowAltCircleRight } from "react-icons/fa";
import Product from '../Product';
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
                    <FaArrowAltCircleLeft id='left'/>
                    <FaArrowAltCircleRight id='right' />
                    </div>
                    </h1>
                    <div className='productline'>
                    {products.filter(product => product.type_id == type.id).map(filteredProducts => (
                        <div className='eachproduct'>
                            <Product id={filteredProducts.id}
                                    typeId={filteredProducts.type_id}
                                    name={filteredProducts.name}
                                    description={filteredProducts.description}
                                    price={filteredProducts.price}
                                    image={filteredProducts.image}
                                    created={filteredProducts.created_at}
                                    updated={filteredProducts.updated_at}
                                    />
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

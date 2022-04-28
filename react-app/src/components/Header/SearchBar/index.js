import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {Link} from 'react'
import SearchIcon from "@mui/icons-material/Search";
import { getProducts } from "../../../store/products";

function SearchBar({setSearchResult, searchResult}) {
    const dispatch = useDispatch()
  const products = useSelector((state) => state?.productReducer);
  const [search, setSearch] = useState([]);



  useEffect(() => {
      dispatch(getProducts())
  }, [])

  useEffect(() => {
      if(search.length > 3) {
          return
      }
  }, [search])

  useEffect(() => {
      let array = []
      console.log(search)
      for(let i = 0; i< products.length; i++) {
         let name = products[i].name.toLowerCase()
         if(name.includes(search)) {
             array.push(products[i])
         }
      }
      setSearchResult(array)
  }, [search]);

  return (
<>
      <input
        className="headersearchinput"
        placeholder="Search by product"
        type="text"
        value={search}
        onChange={e => setSearch(e.target.value)}
        />
        <SearchIcon className="headersearchicon" />

      </>
  );
}

export default SearchBar;

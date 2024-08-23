import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const ProductDetail = () => {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:8000/api/products/${id}/')
            .then(response => setProduct(response.data))
            .catch(error => console.error(error));
    }, [id]);

    if (!product) return <div>Loading...</div>;

       return (
           <div>
               <h1>{product.title}</h1>
               <p>Category: {product.category}</p>
               <p>Price: ₹{product.price}</p>
               <p>MRP: ₹{product.mrp}</p>
               <p>Last 7 Day Sale: ₹{product.last_7_day_sale}</p>
               <p>Fit: {product.fit}</p>
               <p>Fabric: {product.fabric}</p>
               <p>Neck: {product.neck}</p>
               <p>Sleeve: {product.sleeve}</p>
               <p>Pattern: {product.pattern}</p>
               <p>Length: {product.length}</p>
               <p>Description: {product.description}</p>
               <h3>Available SKUs:</h3>
               <ul>
                   {product.available_skus.map((sku, index) => (
                       <li key={index}>
                           Color: {sku.color}, Sizes: {sku.size.join(', ')}
                       </li>
                   ))}
               </ul>
           </div>
       );
   };

   export default ProductDetail;
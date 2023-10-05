import React from "react";

// function Greet(){
//     return <h1>Hello GRP!</h1>
// }

//Replacing the above function as an Arrow Function using the ES-6 format

//Approach 1
// const Greet = () => {
//     return <h1>Hi! GRP!!</h1>
// }

// export default Greet

//Approach 2
// Named Export - When implementing Named Export we must import 
// in App.js with exact Same Name otherwise we will get an Error
export const Greet = () => {
    return <h1>Hi! GRP!!</h1>
}
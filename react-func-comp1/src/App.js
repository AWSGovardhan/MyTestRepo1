// import logo from './logo.svg';
import './App.css';

import { Greet }  from './component/Greet'; //Cannot change name for Named Export
//Also note that in the import statement the component name must be inside curly braces

// import Greet from './component/Greet'; //For default exported components
// import MyFuncComp from './component/Greet' This is for default exported components

// function App() {
//   return (
//     <div className="App">
//       <MyFuncComp />
//     </div>
//   );
// }

// Approach 2
function App() {
  return (
    <div className="App">
      <Greet />
    </div>
  );
}

export default App;

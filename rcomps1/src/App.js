import logo from './logo.svg';
import './App.css';
import Header from './Header'; // Import the Header component
import Footer from './Footer'; // Import the Footer component

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }



export default App;
function App() {
  return (
    <div>
      <Header /> {/* Use the Header component */}
      <main>
        <h1>Hello, World!</h1>
      </main>
      <Footer /> {/* Use the Footer component */}
    </div>
  );
}

// export default App;
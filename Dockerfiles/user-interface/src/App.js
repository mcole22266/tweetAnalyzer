import React from 'react';
import './assets/stylesheets/App.less';

function App() {
  return (
    <div className="container">
      <div className="item app-name">
        TWEET ANALYZER
      </div>
      <div className="item search-bar">
        <form>
          <input type="text" placeholder="Search..." autoFocus className="search-box" required />
          <button className="search-button" type="submit">ANALYZE</button>
        </form>
      </div>
    </div>
  );
}

export default App;

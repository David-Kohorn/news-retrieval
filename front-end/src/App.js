function App() {
  return (
    <div className="App">
      <h1>Search</h1>
        <input type="text" placeholder="Topic of interest..."></input>
        <label for="numbers">How many articles to return?</label>
        <select id="numbers">
          <option value="5">5</option>
          <option value="10">10</option>
          <option value="15">15</option>
          <option value="20">20</option>
        </select>
    </div>
  );
}

export default App;

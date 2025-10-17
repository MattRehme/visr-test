fetch("/get_data")
  .then(r => r.json())
  .then(d => console.log("Received:", d))
  .catch(e => console.error("Fetch error:", e));

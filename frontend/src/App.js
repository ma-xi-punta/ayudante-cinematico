import React, { useState } from "react";

function App() {
  const [vientoReal, setVientoReal] = useState({ intensidad: 0, direccion: 0 });
  const [propulsion, setPropulsion] = useState({ intensidad: 0, direccion: 0 });
  const [vientoRelativo, setVientoRelativo] = useState(null);

  const calcularVientoRelativo = async () => {
    const response = await fetch("http://127.0.0.1:8000/calcular_viento_relativo/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        viento_verdadero: vientoReal,
        propulsion_buque: propulsion,
      }),
    });
    const data = await response.json();
    setVientoRelativo(data.viento_relativo);
  };

  return (
    <div className="App">
      <h1>Calculadora Cinemática</h1>
      <div>
        <h3>Viento Verdadero</h3>
        <input
          type="number"
          placeholder="Intensidad (nudos)"
          value={vientoReal.intensidad}
          onChange={(e) => setVientoReal({ ...vientoReal, intensidad: e.target.value })}
        />
        <input
          type="number"
          placeholder="Dirección (°)"
          value={vientoReal.direccion}
          onChange={(e) => setVientoReal({ ...vientoReal, direccion: e.target.value })}
        />
      </div>

      <div>
        <h3>Propulsión del Buque</h3>
        <input
          type="number"
          placeholder="Intensidad (nudos)"
          value={propulsion.intensidad}
          onChange={(e) => setPropulsion({ ...propulsion, intensidad: e.target.value })}
        />
        <input
          type="number"
          placeholder="Dirección (°)"
          value={propulsion.direccion}
          onChange={(e) => setPropulsion({ ...propulsion, direccion: e.target.value })}
        />
      </div>

      <button onClick={calcularVientoRelativo}>Calcular Viento Relativo</button>

      {vientoRelativo && (
        <div>
          <h3>Viento Relativo:</h3>
          <p>Intensidad: {vientoRelativo.intensidad} nudos</p>
          <p>Dirección: {vientoRelativo.direccion}°</p>
        </div>
      )}
    </div>
  );
}

export default App;

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import MainPage from "./pages/MainPage";

const theme = createTheme({
  typography: {
    fontFamily: "Ubuntu, Arial, sans-serif", // Asegúrate de agregar la fuente aquí
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <Routes>
          <Route path="/" element={<MainPage />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;

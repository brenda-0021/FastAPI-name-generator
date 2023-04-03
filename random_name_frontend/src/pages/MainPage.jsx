import React, { useEffect } from "react";
import {
  Container,
  Typography,
  Grid,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  Button,
} from "@mui/material";
import axios from "axios";

const MainPage = () => {
  const [gender, setGender] = React.useState("");
  const [country, setCountry] = React.useState("");
  const [name, setName] = React.useState("");

  const handleCountry = (event) => {
    setCountry(event.target.value);
  };

  const handleGender = (event) => {
    setGender(event.target.value);
  };

  const createNationality = () => {
    var nationality;
    if (country === "Nepal") {
      return (nationality = "Nepali");
    } else if (country === "Germany") {
      return (nationality = "German");
    } else if (country === "France") {
      return (nationality = "French");
    } else if (country === "United-States") {
      return (nationality = "English");
    } else {
      return (nationality = "none");
    }
  };

  const handleClick = async () => {
    const nationality = createNationality();
    const payload = {
      nationality,
      country,
      gender,
    };
    try
      {const random_name = await axios.get(
        `http://localhost:8000/generate`,
        {params:payload},
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      const data = await random_name.data.random_name;
     setName(data);

    }

    catch (error) {
      const data = await error.data.err_messge;
      setName(data)

    }
  };

  return (
    <>
      <Container
        maxWidth="xl"
        sx={{
          height: "100vh",
          width: "100%",
          backgroundColor: "cyan",
          background: "linear-gradient(to right bottom, #2f4f4f,#54606e)",
        }}
      >
        <Typography
          variant="h3"
          align="center"
          sx={{ color: "#d1d6dc", pt: "2%" }}
        >
          Radnom Name Generator
        </Typography>
        <Container sx={{ padding: "3%", width: "60%" }}>
          <Grid container spacing={2}>
            <Grid item xs={4}>
              <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label" color="warning">
                  Country
                </InputLabel>
                <Select
                  labelId="demo-simple-select-label"
                  id="demo-simple-select"
                  value={country}
                  label="Country"
                  color="warning"
                  onChange={handleCountry}
                >
                  <MenuItem value={"none"}>...</MenuItem>
                  <MenuItem value={"France"}>France</MenuItem>
                  <MenuItem value={"United-States"}>United States</MenuItem>
                  <MenuItem value={"Nepal"}>Nepal</MenuItem>
                  <MenuItem value={"Germany"}>Germany</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={4}>
              <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label" color="warning">
                  Gender
                </InputLabel>
                <Select
                  labelId="demo-simple-select-label"
                  id="demo-simple-select"
                  value={gender}
                  label="Gender"
                  color="warning"
                  onChange={handleGender}
                >
                  <MenuItem value={"none"}>......</MenuItem>
                  <MenuItem value={"Male"}>Male</MenuItem>
                  <MenuItem value={"Female"}>Female</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={4}>
              <Button
                variant="outlined"
                sx={{ height: "60px", width: "120px" }}
                onClick={handleClick}
              >
                Submit
              </Button>
            </Grid>
          </Grid>
        </Container>
        {name ? (
          <Typography align="center" variant="h5">
            Random genereted name is {name}.
          </Typography>
        ) : (
          <></>
        )}
      </Container>
    </>
  );
};

export default MainPage;

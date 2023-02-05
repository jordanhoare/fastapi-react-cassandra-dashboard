// project import
import Routes from 'routes';
import ThemeCustomization from 'themes';
import ScrollTop from 'components/ScrollTop';
import { useEffect } from 'react';
import { useState } from 'react';


const App = () => {

    const [cars, setCars] = useState([]);
    useEffect(() => {
        fetch("/items").then(response => 
            response.json().then(cars => {
                setCars(cars.recent_returns)
                console.log(cars)
            })
            );
    },
    []);

    return (
      <div>
        <ThemeCustomization>
            <ScrollTop>
                <Routes cars={cars} />
            </ScrollTop>
        </ThemeCustomization>
      </div>
    );
  };
  
  export default App;
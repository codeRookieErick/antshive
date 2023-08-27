import {createBrowserRouter, RouterProvider} from 'react-router-dom';
import HomePage from './shared/pages/HomePage';

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage></HomePage>
  }
])

export default function App(){
  return <RouterProvider router={router}/>;
}
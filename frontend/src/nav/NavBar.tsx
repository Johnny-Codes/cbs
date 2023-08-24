import { NavLink } from "react-router-dom";
import { useDispatch } from "react-redux";
import { selectedCoinId } from "../coins/selectedCoinSlice";
import { setEditMode, setAddMode } from "../coins/addOrEditCoinSlice";

const NavBar = () => {
  const dispatch = useDispatch();

  const handleAddCoinClick = () => {
    dispatch(selectedCoinId(null));
  };
  const handleInventoryClick = () => {
    dispatch(setAddMode());
  };
  return (
    <nav className="flex items-center justify-between flex-wrap bg-blue-500 p-6">
      <div className="flex items-center flex-shrink-0 text-white mr-6">
        <span className="font-semibold text-xl tracking-tight">
          <NavLink to="/">coINventory</NavLink>
        </span>
      </div>
      <div className="block lg:hidden">
        <button className="flex items-center px-3 py-2 border rounded text-white-200 border-teal-400 hover:text-white hover:border-white">
          <svg
            className="fill-current h-3 w-3"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <title>Menu</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
          </svg>
        </button>
      </div>
      <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
        <div className="text-sm lg:flex-grow">
          <NavLink
            to="/inventory"
            className="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-gray-500 mr-4"
            onClick={handleInventoryClick}
          >
            Inventory
          </NavLink>
          <NavLink
            to="/add-coin"
            className="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-gray-500 mr-4"
            onClick={handleAddCoinClick}
          >
            Add Coin
          </NavLink>
          {/* <a
            href="#responsive-header"
            className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white"
          >
            Blog
          </a>
        </div>
        <div>
          <a
            href="#"
            className="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0"
          >
            Download
          </a>*/}
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
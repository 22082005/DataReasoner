import "../Navbar/Navbar.css";

function Navbar(){
    return (
        <nav className='navbar'>
            <div className='nav-logo'>DataReasoner</div>
            <div className='nav-links'>
                <a href="/">Home</a>
                <a href ="/">Documentation</a>
                <a href ="/">Github</a>
            </div>
        </nav>
    )
}

export default Navbar;
import React, { useState, useEffect } from "react";
import { AboutModal } from "../../context/AboutModal";

function About() {
  const [showMenu, setShowMenu] = useState(false);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  return (
    <>
      <button className="about-me" onClick={() => setShowModal(true)}>
        About
      </button>
      {showModal && (
        <AboutModal onClose={() => setShowModal(false)}>
          <div>
            <div>
              <h3 className="project-info">
                A simple react clone of Yelp
              </h3>
            </div>

          </div>
        </AboutModal>
      )}
    </>
  );
}

export default About;

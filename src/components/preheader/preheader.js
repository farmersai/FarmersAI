import React from "react";
import "./preheader.css";

const PreHeader = () => {
  const width = window.innerWidth;
  console.log(width);
  return (
    <div className="bg-[#FFFFFF] px-6 py-1 md:inline-block hidden w-full">
      <div className="flex justify-between items-center ml-6">
        <div className="flex justify-center items-center">
          
        </div>
        <div className="">
          <div className="" id="google_element"></div>
        </div>
      </div>
    </div>
  );
};

export default PreHeader;

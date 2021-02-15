import "./ImageComponent.css";
import React, { useState } from "react";

function ImageComponent(props) {
  // const { imageUrl } = props;
  const imageUrl = "./images/10x.jpg";
  return (
    <div className="imageparent">
      <img src={`http://54.210.86.248/:9000/${props.img}`} className="imagecompo" />
    </div>
  );
}

// export default ImageComponent;

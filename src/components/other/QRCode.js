import React from "react";
import { Space, theme, Input } from "antd";

import { QRCodeCanvas } from "qrcode.react";

const Invite = () => {
  const [text, setText] = React.useState(
    "https://twitter.com/intent/tweet?text=doogle"
  );
  return (
    <QRCodeCanvas
      style={{
        width: "auto",
        justifyContent: "center",
        alignItems: "center",
        display: "flex",
      }}
      value={"https://picturesofpeoplescanningqrcodes.tumblr.com/"}
      title={"Title for my QR Code"}
      size={128}
      bgColor={"#ffffff"}
      fgColor={"#000000"}
      level={"L"}
      imageSettings={{
        src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXer1sD5Dida5ynDCUj2bnJzAsETYQYqM22Vd8lBVaem3DH6eRSGx5vfY&s",
        x: undefined,
        y: undefined,
        height: 24,
        width: 24,
        opacity: 1,
        excavate: true,
      }}
    />
    // <Space direction="vertical" align="center">
    //   <QRCodeCanvas value={text || "-"} />
    //   <Input
    //     placeholder="-"
    //     maxLength={60}
    //     value={text}
    //     onChange={(e) => setText(e.target.value)}
    //   />
    // </Space>
  );
};
export default Invite;

import React, { useState } from "react";
import { Radio } from "antd";
const AccontTypeSelection = ({ onTypeChange }) => {
  const [value, setValue] = useState(1);
  const onChange = (e) => {
    console.log("radio checked", e.target.value);
    setValue(e.target.value);
    onTypeChange(e.target.value);
  };
  return (
    <Radio.Group onChange={onChange} value={value}>
      <Radio value={1}>Individual</Radio>
      <Radio value={2}>Family</Radio>
    </Radio.Group>
  );
};
export default AccontTypeSelection;

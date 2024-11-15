import React, { useEffect, useState } from "react";
import { Modal } from "antd";
import { useHistory } from "react-router-dom";
import { Button, Form, Input, Select } from "antd";
import axios from "axios";
import { DatePicker } from "antd";
import dayjs from "dayjs";
import customParseFormat from "dayjs/plugin/customParseFormat";
import "../../assets/styles/information.css";

dayjs.extend(customParseFormat);
const { Option } = Select;
const dateFormat = "YYYY-MM-DD";
const FamilyInformation = (userId) => {
  const history = useHistory();
  const [open, setOpen] = useState(false);
  const formatDate = (dateString) => {
    // Create a new Date object from the provided date string
    const date = new Date(dateString);

    // Get the year, month, and day from the Date object
    const year = date.getFullYear();
    const month = ("0" + (date.getMonth() + 1)).slice(-2); // Months are zero-based
    const day = ("0" + date.getDate()).slice(-2);

    // Combine the parts into the desired format
    return `${year}-${month}-${day}`;
  };
  const showModal = () => {
    setOpen(true);
  };
  useEffect(() => {
    showModal();
  }, []);

  const handleFamilySubmit = async (userData) => {
    // const response = await axios.post(
    //   "https://doogle-1c3b68536bb7.herokuapp.com/user/update",
    //   { userData: userData },
    //   {
    //     headers: {
    //       "Content-Type": "application/json",
    //       "Access-Control-Allow-Origin": "*",
    //     },
    //   }
    // );
    // console.log("Response:", response.data);
    // if (response.data.status === "success") {
    history.push("/dashboard");
    // }
  };
  const handleCancel = () => {
    setOpen(false);
  };

  const onFinish = (values) => {
    console.log("Success:", values);

    const date = formatDate(values.age._d);

    // const userData = {
    //   gender: values.gender,
    //   birth_date: date,
    //   address: values.address,
    //   occupation: values.occupation,
    //   income_source: values.income,
    //   userId: userId.userId,
    //   goal: values.goal,
    // };

    // handleFamilySubmit(userData);
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };
  return (
    <Modal
      open={open}
      title="Please enter family Info"
      onCancel={handleCancel}
      footer={
        [
          // <Button key="back" onClick={handleCancel}>
          //   Return
          // </Button>,
          // <Button
          //   key="submit"
          //   type="primary"
          //   loading={loading}
          //   onClick={handleOk}
          //   onSubmit={handleSubmit}
          // >
          //   Submit
          // </Button>,
        ]
      }
    >
      <Form
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        layout="vertical"
        className="row-col"
      >
        <Form.Item
          className="username"
          label="Household Members"
          name="householdMembers"
          rules={[
            {
              required: true,
              message: "Please input the number of household members!",
            },
          ]}
        >
          <Input placeholder="Number of household members" type="number" />
        </Form.Item>

        <Form.Item
          className="username"
          label="Total Household Income (Monthly)"
          name="totalIncome"
          rules={[
            {
              required: true,
              message: "Please input your total household income!",
            },
          ]}
        >
          <Input placeholder="Total household income" prefix="$" />
        </Form.Item>

        <Form.Item
          className="username"
          label="Main Source of Income"
          name="incomeSource"
          rules={[
            {
              required: true,
              message: "Please select the main source of income!",
            },
          ]}
        >
          <Select placeholder="Select main income source">
            <Option value="employment">Employment</Option>
            <Option value="business">Business</Option>
            <Option value="investments">Investments</Option>
            <Option value="retirement">Retirement Funds</Option>
            <Option value="other">Other</Option>
          </Select>
        </Form.Item>

        <Form.Item
          className="username"
          label="Monthly Living Expenses"
          name="livingExpenses"
          rules={[
            {
              required: true,
              message: "Please input your monthly living expenses!",
            },
          ]}
        >
          <Input placeholder="Monthly living expenses" prefix="$" />
        </Form.Item>

        <Form.Item
          className="username"
          label="Financial Goals"
          name="financialGoals"
          rules={[
            {
              required: true,
              message: "Please select your financial goals!",
            },
          ]}
        >
          <Select placeholder="Select financial goals" mode="multiple">
            <Option value="saving">Saving for Retirement</Option>
            <Option value="education">Children's Education</Option>
            <Option value="home">Buying a Home</Option>
            <Option value="travel">Travel</Option>
            <Option value="investment">Investment</Option>
            <Option value="debtReduction">Debt Reduction</Option>
          </Select>
        </Form.Item>

        <Form.Item
          className="username"
          label="Do you have any debts?"
          name="debts"
          rules={[
            {
              required: true,
              message: "Please select an option!",
            },
          ]}
        >
          <Select placeholder="Select an option">
            <Option value="yes">Yes</Option>
            <Option value="no">No</Option>
          </Select>
        </Form.Item>

        <Form.Item
          className="username"
          label="Investment and Saving Plans"
          name="investmentPlans"
          rules={[
            {
              required: true,
              message: "Please input details about your investment plans!",
            },
          ]}
        >
          <Input.TextArea placeholder="Describe your investment and saving plans" />
        </Form.Item>

        <Form.Item>
          <Button
            style={{ width: "100%", marginTop: "20px" }}
            type="primary"
            htmlType="submit"
            onClick={handleFamilySubmit}
          >
            Submit
          </Button>
        </Form.Item>
      </Form>
    </Modal>
  );
};

export default FamilyInformation;

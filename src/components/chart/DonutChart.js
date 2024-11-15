import React, { useState, useEffect } from "react";
import Chart from "react-apexcharts";
const months = [
  { value: 1, label: "Jan" },
  { value: 2, label: "Feb" },
  { value: 3, label: "Mar" },
  { value: 4, label: "Apr" },
  { value: 5, label: "May" },
  { value: 6, label: "Jun" },
  { value: 7, label: "Jul" },
  { value: 8, label: "Aug" },
  { value: 9, label: "Sep" },
  { value: 10, label: "Oct" },
  { value: 11, label: "Nov" },
  { value: 12, label: "Dec" },
];
const DonutChart = ({
  type,
  month,
  year,
  registrationMonth,
  registrationYear,
  incomeData,
  expenseData,
}) => {
  const expenseInitialData = [
    { type: "Housing", value: 8 },
    { type: "Food", value: 9 },
    { type: "Transportation", value: 10 },
    { type: "Entertainment", value: 11 },
    { type: "Utilities", value: 12 },
    { type: "Health", value: 13 },
    { type: "Insurance", value: 14 },
    { type: "Education", value: 15 },
    { type: "Other Expenses", value: 16 },
    { type: "Investment Expens", value: 17 },
    { type: "Shopping", value: 18 },
    { type: "Grocery", value: 19 },
  ];
  const incomeInitialData = [
    { type: "Salary", value: 10000 },
    { type: "Bonus", value: 3000 },
    { type: "Investment Income", value: 2000 },
    { type: "Other Income", value: 0 },
    { type: "Business", value: 0 },
    { type: "Part-time Job", value: 1000 },
    { type: "Buying and Selling", value: 1000 },
  ];
  const EmptyIncome = [
    { type: "Salary", value: 0 },
    { type: "Bonus", value: 0 },
    { type: "Investment Income", value: 0 },
    { type: "Other Income", value: 0 },
    { type: "Business", value: 0 },
    { type: "Part-time Job", value: 0 },
    { type: "Buying and Selling", value: 0 },
  ];
  const EmptyExpense = [
    { type: "Housing", value: 0 },
    { type: "Food", value: 0 },
    { type: "Transportation", value: 0 },
    { type: "Entertainment", value: 0 },
    { type: "Utilities", value: 0 },
    { type: "Health", value: 0 },
    { type: "Insurance", value: 0 },
    { type: "Education", value: 0 },
    { type: "Other Expenses", value: 0 },
    { type: "Investment Expens", value: 0 },
    { type: "Shopping", value: 0 },
    { type: "Grocery", value: 0 },
  ];

  const initialData =
    type === "income" ? incomeInitialData : expenseInitialData;

  const [data, setData] = useState(initialData);

  useEffect(() => {
    setData(
      type === "income"
        ? incomeData && incomeData.length > 0
          ? incomeData
          : EmptyIncome
        : expenseData && expenseData.length > 0
        ? expenseData
        : EmptyExpense
    );
    // if (month && year && registrationMonth && registrationYear) {
    //   const currentDate = new Date();
    //   const currentMonth = currentDate.getMonth() + 1;
    //   const currentYear = currentDate.getFullYear();
    //   if (currentYear < year || registrationYear > year) {
    //     type === "expense" ? setData(EmptyExpense) : setData(EmptyIncome);
    //   }
    //   if (registrationMonth > month || currentMonth < month) {
    //     type === "expense" ? setData(EmptyExpense) : setData(EmptyIncome);
    //   }
    // } else {
    //   console.log("Get in here");
    //   setData(
    //     type === "income"
    //       ? incomeData || EmptyIncome
    //       : expenseData || EmptyExpense
    //   );
    //   console.log("data", data);
    // }
  }, [type, incomeData, expenseData]);

  const series = data.map((item) => item.value);
  const labels = data.map((item) => item.type);

  const config = {
    chart: {
      type: "donut",
      events: {
        dataPointSelection: function (event, chartContext, config) {
          const selectedLabel = config.w.globals.labels[config.dataPointIndex];
          const selectedValue = config.w.globals.series[config.dataPointIndex];
          const totalValue = config.w.globals.seriesTotals.reduce(
            (a, b) => a + b,
            0
          );
          const selectedPercentage = (
            (selectedValue / totalValue) *
            100
          ).toFixed(1);
          chartContext.updateOptions(
            {
              plotOptions: {
                pie: {
                  donut: {
                    labels: {
                      total: {
                        show: true,
                        showAlways: true,
                        label: selectedLabel,
                        formatter: function () {
                          return `${selectedPercentage}%`;
                        },
                      },
                    },
                  },
                },
              },
            },
            false,
            false
          );
        },
      },
    },
    plotOptions: {
      pie: {
        donut: {
          labels: {
            show: true,
            name: {
              show: true,
              fontSize: "22px",
              fontFamily: "Helvetica, Arial, sans-serif",
              fontWeight: 600,
              color: "#373d3f",
              offsetY: -10,
            },
            value: {
              show: true,
              fontSize: "16px",
              fontFamily: "Helvetica, Arial, sans-serif",
              fontWeight: 400,
              color: "#373d3f",
              offsetY: 16,
              formatter: function (val) {
                return val;
              },
            },
            total: {
              show: true,
              showAlways: true,
              label: "Total",
              fontSize: "22px",
              fontFamily: "Helvetica, Arial, sans-serif",
              fontWeight: 600,
              color: "#373d3f",
              formatter: function (w) {
                return w.globals.seriesTotals.reduce((a, b) => a + b, 0);
              },
            },
          },
        },
      },
    },
    labels: labels,
    series: series,
    responsive: [
      {
        breakpoint: 480,
        options: {
          chart: {
            width: 200,
          },
          legend: {
            position: "bottom",
          },
        },
      },
    ],
  };

  return (
    <div>
      <Chart
        options={config}
        series={config.series}
        type="donut"
        width="100%"
        height="600px"
      />
    </div>
  );
};

export default DonutChart;

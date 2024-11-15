import React, { useState } from 'react';
import {
  Card,
  Col,
  Row,
  Typography,
  Space,
  Table,
  Carousel,
  Select,
} from 'antd';

const { Title } = Typography;

const months = [
  { value: '1', label: 'Jan' },
  { value: '2', label: 'Feb' },
  { value: '3', label: 'Mar' },
  { value: '4', label: 'Apr' },
  { value: '5', label: 'May' },
  { value: '6', label: 'Jun' },
  { value: '7', label: 'Jul' },
  { value: '8', label: 'Aug' },
  { value: '9', label: 'Sep' },
  { value: '10', label: 'Oct' },
  { value: '11', label: 'Nov' },
  { value: '12', label: 'Dec' },
];

const years = Array.from({ length: 25 }, (_, index) => ({
  value: (2000 + index).toString(),
  label: (2000 + index).toString(),
}));

const fakeFinanceData = [
  {
    key: '1',
    category: 'International Organization for Migration',
    amount: 20,
  },
  { key: '2', category: 'United Nations Population Fund', amount: 400 },
  { key: '3', category: 'World Food Programme', amount: 50 },
];

const fakeStudyData = [
  {
    key: '1',
    category: 'Introduction to Personal Finance',
    amount: 2,
  },
  { key: '2', category: 'Basic Budgeting Techniques', amount: 4 },
];

const columns = [
  { title: 'Name', dataIndex: 'category', key: 'category' },
  { title: 'Amount', dataIndex: 'amount', key: 'amount' },
  {
    title: 'Action',
    key: 'action',
    render: () => (
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <a>Details</a>
        <a>Donate</a>
      </div>
    ),
  },
];

const columns1 = [
  { title: 'Name', dataIndex: 'category', key: 'category' },
  { title: 'Time(h)', dataIndex: 'amount', key: 'amount' },
  {
    title: 'Action',
    key: 'action',
    render: () => (
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <a>Details</a>
        <a>Study</a>
      </div>
    ),
  },
];

const cardData = [
  {
    title: 'Introduction to Personal Finance',
    message: "A beginner's guide to managing personal finances effectively.",
    link: 'https://gnec.ngo/',
  },
  {
    title: 'Basic Budgeting Techniques',
    message:
      'Learn essential budgeting skills to better control your expenses.',
    link: 'https://gnec.ngo/',
  },
  {
    title: 'Foundations of Investment',
    message: 'Understand the basics of investing.',
    link: 'https://gnec.ngo/',
  },
];

function Donation() {
  const [month, setMonth] = useState('1');
  const [year, setYear] = useState('2024');

  const count = [
    {
      today: 'Donate Now',
      title: '$40,000',
      color: '#28a745',
      info: 'support people affected by the Türkiye-Syria Earthquakes',
      link: 'https://www.un.org/en/turkiye-syria-earthquake-response',
    },
    {
      today: 'Donate Now',
      title: '$88,000',
      color: '#28a745',
      info: 'support people affected by the Ukraine crisis',
      link: 'https://news.un.org/en/focus/ukraine/donate?_gl=1*1tok7lg*_ga*NzYyODIyNzE5LjE3MzE1ODY4NTY.*_ga_TK9BQL5X7Z*MTczMTU4Njg1NS4xLjEuMTczMTU4NzE0MC4wLjAuMA..',
    },
  ];

  const budgetData = {
    today: 'Monthly Donate Budget',
    title: '$200',
    color: '#28a745',
    info: "Let's build a better future together💚",
  };

  const getMonthLabel = (monthValue) => {
    const monthObj = months.find((m) => m.value === monthValue);
    return monthObj ? monthObj.label : 'Invalid month';
  };
  const label = getMonthLabel(month);

  return (
    <>
      <div className="layout-content">
        <div className="title">Donate</div>
        <Carousel arrows infinite={false} autoplay>
          {count.map((c, index) => (
            <div key={index}>
              <div className="card-container">
                <Card bordered={false} className="criclebox card-uniform">
                  <div className="number">
                    <Row align="middle" gutter={[24, 0]}>
                      <Col xs={18}>
                        <span>{c.today}</span>
                        <h3 style={{ color: c.color }}>{c.title}</h3>
                        <div style={{ whiteSpace: 'pre-line' }}>{c.info}</div>
                        <a
                          href={c.link}
                          style={{
                            color: '#1890ff',
                            textDecoration: 'underline',
                          }}
                        >
                          Learn more
                        </a>
                      </Col>
                    </Row>
                  </div>
                </Card>
              </div>
            </div>
          ))}
        </Carousel>

        <div className="card-container">
          <Card bordered={false} className="criclebox card-uniform">
            <div className="number">
              <Row align="middle" gutter={[24, 0]}>
                <Col xs={18}>
                  <span>{budgetData.today}</span>
                  <h3 style={{ color: budgetData.color }}>
                    {budgetData.title}
                  </h3>
                  <div>
                    <a href="https://gnec.ngo/">{budgetData.info}</a>
                  </div>
                </Col>
              </Row>
            </div>
          </Card>
        </div>

        <div className="card-container">
          <Row gutter={[24, 0]}>
            <p>🔆 Your total support Program🔆</p>
            <Table
              className="card-uniform"
              columns={columns.map((col) => ({
                ...col,
                onCell: () => ({
                  style: { whiteSpace: 'pre-line' },
                }),
              }))}
              dataSource={fakeFinanceData}
            />
          </Row>
        </div>

        <div className="title">Free Study</div>
        <div className="card-container">
          <Card bordered={false} className="criclebox card-uniform">
            <div className="number">
              <Row align="middle" gutter={[24, 0]}>
                <Col xs={18}>
                  <span>Monthly Finance Study Time</span>
                  <h3 style={{ color: budgetData.color }}>25h</h3>
                  <div>
                    <a href="https://gnec.ngo/">
                      Well done! You're making progress! 🥳
                    </a>
                  </div>
                </Col>
              </Row>
            </div>
          </Card>
        </div>
        <div className="card-container">
          <Row gutter={[16, 16]}>
            {cardData.map((data, index) => (
              <Col xs={24} sm={12} key={index}>
                <Card bordered={false} className="criclebox card-uniform">
                  <div className="number">
                    <Row align="middle" gutter={[24, 0]}>
                      <Col xs={20}>
                        <span>{data.title}</span>
                        <p>{data.message}</p>
                        <div>
                          <a href={data.link}>study now</a>
                        </div>
                      </Col>
                    </Row>
                  </div>
                </Card>
              </Col>
            ))}
          </Row>
        </div>

        <div className="card-container">
          <Row gutter={[24, 0]}>
            <p>🔆 Your total Study Program🔆</p>
            <Table
              className="card-uniform"
              columns={columns1.map((col) => ({
                ...col,
                onCell: () => ({
                  style: { whiteSpace: 'pre-line' },
                }),
              }))}
              dataSource={fakeStudyData}
            />
          </Row>
        </div>
      </div>
    </>
  );
}

export default Donation;

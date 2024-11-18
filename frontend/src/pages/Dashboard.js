import React, { useEffect, useState } from 'react';
import { getAccounts, getPosts } from '../services/api';

const Dashboard = () => {
  const [accounts, setAccounts] = useState([]);
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const accountsRes = await getAccounts();
      const postsRes = await getPosts();
      setAccounts(accountsRes.data);
      setPosts(postsRes.data);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <h2>Social Media Accounts</h2>
      <ul>
        {accounts.map((account) => (
          <li key={account.id}>{account.platform}</li>
        ))}
      </ul>
      <h2>Scheduled Posts</h2>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.content} - {post.scheduled_time}</li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;

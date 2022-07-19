import fetch from 'node-fetch';

const SERVERURL = 'http://127.0.0.1:8000/';

export async function getAllPostsData() {
  const rest = await fetch(new URL(`${SERVERURL}api/post/`));
  const posts = await rest.json();
  return posts;
}

export async function getAllPostsIds() {
  const rest = await fetch(new URL(`${SERVERURL}api/post/`));
  const posts = await rest.json();
  return posts.map(post => {
    return {
      params: {
        id: String(post.id),
      },
    };
  });
}

export async function getPostData(id) {
  const res = await fetch(new URL(`${SERVERURL}api/post/${id}`));
  const post = await res.json();
  return post;
}

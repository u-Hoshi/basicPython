import { useRouter } from 'next/router';
import { getAllPostsIds, getPostData } from '../../lib/posts';

export default function PostData({ post }) {
  const router = useRouter();

  if (router.isFallback || !post) return <div>loading...</div>;
  return (
    <div className='space-y-5 w-full'>
      <div className='flex justify-center flex-col items-center mb-5'>
        <h1 text-3xl mb-3 font-bold>
          {post.title}
        </h1>
        <p className='mb-3'>{post.created_at}</p>
        <div className='border w-14'></div>
      </div>
      <p className='whitespace-pre-wrap'>{post.content}</p>
    </div>
  );
}

// SSG用の関数 動的なルーティンの利用時に静的ファイルを作成(投稿一覧のIDを取得)
export async function getStaticPaths() {
  const paths = await getAllPostsIds();
  return {
    paths,
    fallback: true,
  };
}

export async function getStaticProps({ params }) {
  const post = await getPostData(params.id);
  return {
    props: {
      post,
    },
    revalidate: 3,
  };
}

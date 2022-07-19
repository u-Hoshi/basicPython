import Link from 'next/link';

export default function Post({ post }) {
  return (
    <Link href={`posts/${post.id}`}>
      <div className='p-4 cursor-pointer sm:w-1/2 lg:w-1/4'>
        <img src={post.image} alt='post' className='object-cover' />
        <div className='text-center my-4'>
          <p>{post.title}</p>
        </div>
      </div>
    </Link>
  );
}

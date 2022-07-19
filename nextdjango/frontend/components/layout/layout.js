import Navigation from './navigation';

export default function Layout(props) {
  return (
    <div className='flex flex-col min-h-screen'>
      <Navigation />
      <main className='container flex flex-1 justify-center mx-auto px-5 max-w-screen-lg'>
        {props.children}
        {/*  {props.children} によって各要素の中身が入り動的に切り替わる */}
      </main>
    </div>
  );
}

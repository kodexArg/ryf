export async function load({ fetch, params }) {
  const source = '/characters.json';
  const { slug } = params;
  const res = await fetch(source);
  const json = await res.json();

  const character = json.characters.find(item => item.slug === slug);

  if (character) {
    return { props: { character } };
  } else {
    return { status: 404, error: new Error('Character not found') };
  }
}
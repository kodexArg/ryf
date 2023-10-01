import tailwind from 'tailwindcss'
import autoprefixer from 'autoprefixer'

export default  {
    syntax: 'postcss-scss',
    plugins: [
        // Some plugins, like postcss-nested, need to run before Tailwind
        tailwind(),

        autoprefixer(),
        // !dev &&
        //  cssnano({
        //      preset: 'default',
        //  }),
    ],
};
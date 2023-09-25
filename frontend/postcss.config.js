import nesting from '@tailwindcss/nesting'
import tailwind from 'tailwindcss'
import autoprefixer from 'autoprefixer'

export default  {
    syntax: 'postcss-scss',
    plugins: [
        // Some plugins, like postcss-nested, need to run before Tailwind
        nesting(),
        tailwind(),

        autoprefixer(),
        // !dev &&
        //  cssnano({
        //      preset: 'default',
        //  }),
    ],
};
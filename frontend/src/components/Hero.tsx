export default function Hero() {
  return (
    <section className="text-center py-24 space-y-6">
      <h2 className="text-4xl font-bold">
        Learn smarter with AI‑powered education
      </h2>

      <p className="max-w-xl mx-auto text-muted-foreground">
        Free & paid courses, AI tutor, analytics dashboard and automated
        feedback powered by microservices.
      </p>

      <div className="flex flex-wrap justify-center gap-4">
        <button className="rounded-full bg-slate-900 px-6 py-3 text-white transition hover:bg-slate-700">
          Explore courses
        </button>
        <button className="rounded-full border border-slate-900 px-6 py-3 text-slate-900 transition hover:bg-slate-50">
          Get started
        </button>
      </div>
    </section>
  )
}
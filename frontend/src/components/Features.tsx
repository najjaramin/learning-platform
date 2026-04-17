const features = [
  {
    title: "AI Tutor",
    description: "Ask questions, get explanations and generate quizzes.",
  },
  {
    title: "Microservices",
    description: "FastAPI, Node.js, Docker and API Gateway.",
  },
  {
    title: "Analytics",
    description: "Track enrollments, progress and trends.",
  },
]

export default function Features() {
  return (
    <section className="grid md:grid-cols-3 gap-6 py-16">
      {features.map((f, i) => (
        <div key={i} className="border rounded-2xl p-6">
          <h3 className="text-lg font-semibold">{f.title}</h3>
          <p className="text-muted-foreground mt-2">{f.description}</p>
        </div>
      ))}
    </section>
  )
}
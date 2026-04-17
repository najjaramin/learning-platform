export default function CoursesPreview() {
  return (
    <section className="py-16">
      <h3 className="text-2xl font-bold text-center mb-8">
        Popular courses
      </h3>

      <div className="grid md:grid-cols-3 gap-6">
        {[1, 2, 3].map((i) => (
          <div key={i} className="border rounded-xl p-4">
            <h4 className="font-semibold">Course {i}</h4>
            <p className="text-muted-foreground text-sm">
              Course description preview.
            </p>
          </div>
        ))}
      </div>
    </section>
  )
}
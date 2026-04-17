import Navbar from "@/components/Navbar"
import Hero from "@/components/Hero"
import Features from "@/components/Features"
import CoursesPreview from "@/components/CoursesPreview"
import Footer from "@/components/Footer"

export default function HomePage() {
  return (
    <>
      <Navbar />
      <main className="max-w-6xl mx-auto px-6">
        <Hero />
        <Features />
        <CoursesPreview />
      </main>
      <Footer />
    </>
  )
}
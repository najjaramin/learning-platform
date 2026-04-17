"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function RegisterForm() {
  const router = useRouter()

  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("")
  const [birthDate, setBirthDate] = useState("")
  const [idNumber, setIdNumber] = useState("")
  const [role, setRole] = useState("student")
  const [specialite, setSpecialite] = useState("")
  const [error, setError] = useState("")

  // ✅ calcul âge
  const calculateAge = (date: string) => {
    const birth = new Date(date)
    const today = new Date()
    let age = today.getFullYear() - birth.getFullYear()
    const m = today.getMonth() - birth.getMonth()
    if (m < 0 || (m === 0 && today.getDate() < birth.getDate())) {
      age--
    }
    return age
  }

  // ✅ handle submit
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError("")

    // confirm password
    if (password !== confirmPassword) {
      setError("Passwords do not match")
      return
    }

    // age validation
    const age = calculateAge(birthDate)
    if (age < 19) {
      setError("Age must be 19 or older")
      return
    }

    // ID validation
    if (idNumber.length !== 8) {
      setError("ID number must contain exactly 8 digits")
      return
    }

    // 🔁 appel backend (exemple)
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/auth/register`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          firstName,
          lastName,
          email,
          password,
          birthDate,
          idNumber,
          role,
          specialite,
        }),
      }
    )

    if (!res.ok) {
      setError("Registration failed")
      return
    }

    // ✅ REDIRECT vers page accueil / courses
    router.push("/") // ou "/courses"
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {error && (
        <p className="text-red-500 text-sm text-center">{error}</p>
      )}

      <Input
        placeholder="First name"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
        required
      />

      <Input
        placeholder="Last name"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
        required
      />

      <Input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <Input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />

      <Input
        type="password"
        placeholder="Confirm password"
        value={confirmPassword}
        onChange={(e) => setConfirmPassword(e.target.value)}
        required
      />

      <Input
        type="date"
        value={birthDate}
        onChange={(e) => setBirthDate(e.target.value)}
        required
      />

      <Input
        placeholder="ID number (8 digits)"
        value={idNumber}
        onChange={(e) =>
          setIdNumber(e.target.value.replace(/\D/g, "").slice(0, 8))
        }
        required
      />

      <select
        value={role}
        onChange={(e) => setRole(e.target.value)}
        className="w-full border rounded-md px-3 py-2 text-sm"
      >
        <option value="student">Student</option>
        <option value="instructor">Instructor</option>
      </select>

      <select
        value={specialite}
        onChange={(e) => setSpecialite(e.target.value)}
        className="w-full border rounded-md px-3 py-2 text-sm"
        required
      >
        <option value="">Select spécialité</option>
        <option value="TI">Technologie Informatique</option>
        <option value="GC">Génie Civil</option>
        <option value="GE">Génie Électrique</option>
        <option value="GM">Génie Mécanique</option>
      </select>

      <Button type="submit" className="w-full">
        Create account
      </Button>
    </form>
  )
}
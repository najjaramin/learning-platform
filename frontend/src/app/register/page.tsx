import RegisterForm from "@/components/auth/RegisterForm"

export default function RegisterPage() {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="w-full max-w-md p-6 border rounded-xl">
        <h1 className="text-2xl font-bold mb-6 text-center">
          Create account
        </h1>
        <RegisterForm />
      </div>
    </div>
  )
}